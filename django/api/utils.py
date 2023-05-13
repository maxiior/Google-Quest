import torch
from .constants import response_keys

MAX_LENGTH_T = 30
MAX_LENGTH_Q = 128
MAX_LENGTH_A = 128
MAX_SEQUENCE = 290

category_dict = {
    'LIFE_ARTS': 0,
    'STACKOVERFLOW': 1,
    'TECHNOLOGY': 2,
    'SCIENCE': 3,
    'CULTURE': 4
}

def get_merged(data):
    T = data["question_title"]
    Q = data["question_body"]
    A = data["answer"]
    merged = T.split()[:MAX_LENGTH_T] + Q.split()[:MAX_LENGTH_Q] + A.split()[:MAX_LENGTH_A]
    try:
        C = category_dict[data['category'].upper()]
    except:
        C = 0
    return " ".join(i for i in merged), C

def tokenize(tokenizer, text, category):
    text = tokenizer(
        [text],
        max_length=MAX_SEQUENCE,
        padding='max_length',
        truncation=True,
        return_token_type_ids=False,
        return_tensors='pt'
    )
    return text, torch.tensor([category]).type(torch.float)

def make_dict(scores, data):
    x = {i:j for i,j in zip(response_keys, scores)}
    x['question_title'] = data['question_title']
    x['question_body'] = data['question_body']
    x['answer'] = data['answer']
    x['category'] = data['category']
    return x
