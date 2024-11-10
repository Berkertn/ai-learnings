from transformers import pipeline
import torch

translator = pipeline(task="translation",
                      model="./models/facebook/nllb-200-distilled-600M",
                      torch_dtype=torch.bfloat16)