from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import torch
from transformers import AutoTokenizer, AutoModel
from .architectures import Model, BERT_2FC

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

@api_view(['POST'])
def make_prediction(request):
    data = request.data
    if 'content' in data:
        tokens = T.batch_encode_plus(
                [data['content']],
                max_length=250,
                padding='max_length',
                truncation=True,
                return_token_type_ids=False
            )
        
        input_ids = torch.tensor(tokens['input_ids'])
        mask = torch.tensor(tokens['attention_mask'])
        preds = M(input_ids.to(DEVICE), mask.to(DEVICE))
        
        return Response({"answer": str(preds.detach().numpy())}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)