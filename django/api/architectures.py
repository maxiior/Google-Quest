import torch
from torch import nn

class Model(nn.Module):
    def __init__(self, roberta):
        super(Model, self).__init__()
        self.roberta = roberta
        self.linear1 = nn.Linear(768, 30)

    def forward(self, x):
        x = self.roberta(x).last_hidden_state
        x = torch.mean(x, axis=1)
        x = self.linear1(x)

        return x

class BERT_2FC(nn.Module):
    def __init__(self, bert, input_size=768, hidden_size=512):
        super(BERT_2FC, self).__init__()
        self.bert = bert
        self.dropout = nn.Dropout(0.1)
        self.relu = nn.ReLU()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, 2)
        self.softmax = nn.LogSoftmax(dim=1)
    
    def forward(self, sent_id, mask):
        x = self.bert(sent_id, attention_mask=mask)
        x = self.fc1(x.pooler_output)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x