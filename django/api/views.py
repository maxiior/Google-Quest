from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import torch
from transformers import AutoTokenizer, AutoModel
from .architectures import Model, BERT_2FC
from .utils import tokenize, get_merged, make_dict
from .models import Score
from .constants import response_keys

BERT_MODEL = "allegro/herbert-base-cased" # "roberta-base"
DEVICE = 'cpu'

def get_model():
    device = torch.device(DEVICE)  # or 'cuda' if available
    roberta = AutoModel.from_pretrained(BERT_MODEL).to(device)
    model = BERT_2FC(roberta)   # Model
    x = torch.load('./api/models/model1.pt', map_location=device)
    model.load_state_dict(x)
    tokenizer = AutoTokenizer.from_pretrained(BERT_MODEL)
    model.eval()
    return model, tokenizer

M, T = get_model()

@api_view(['POST', 'GET'])
def predictions(request):
    if request.method == 'POST':

        data = request.data

        if all(key in data for key in ['question_title', 'question_body', 'answer', 'category']):
            text, category = get_merged(data)
            text, category = tokenize(T, text, category)
            preds = M(text['input_ids'].to(DEVICE), text['attention_mask'].to(DEVICE))

            # after updating the model, preds should go to make_dict
            response = make_dict([0 for _ in range(30)], data)

            score = Score(**response)
            score.save()

            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        scores = Score.objects.all()
        response = [{j:getattr(i, j) for j in response_keys} for i in scores]   
        return Response(response, status=status.HTTP_200_OK)