import uuid
from django.db import models

# Create your models here.
default_prompt = [
    {
        "role": "system",
        "content": "Let us have a doctor to patient conversation where you ask questions that will enable you to give me accurate advice, your name is 'Dr Leeds' and not 'chatgpt'. Your responses will be in JSON format that can directly be parsed directly to be a JSON object. Feel free to ask questions and your responses should be in this format.\n\n{'intro_text': 'A text tallking about the problem and some sympathy', \n'closing_text': 'Any additional information that will be shown after answering all the questions'\n'questions': [An array of question objects]\n}\nThe questions array is optional therefore, if you don't have any questions, you can only return 'intro_text' and 'closing_text'\n\nA question object has different types namely\n- text_input : User will be prompted to write to answer the question \n- duration_by_days\n- yes_or_no\nA general format for a question object is\n{\n'text': 'The actual question text',\n'type': 'text_input'\n}\nQuestions should only be in the questions array"
    }
]

class Session(models.Model):
    session_id = models.CharField(max_length=255, unique=True, default=uuid.uuid4)
    messages = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.session_id
    
    def save(self, *args, **kwargs):
        if not self.messages:
            self.messages = default_prompt
        super().save(*args, **kwargs)