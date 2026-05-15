from groq import Groq, APIConnectionError, APIStatusError
from app.config import config_setting
from typing import List
from fastapi.exceptions import HTTPException

client = Groq(api_key=config_setting.GROQ_API_KEY)

def user_answer(question: str, chunkList: List[str]) -> str:
    context = ''.join(chunkList)
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    'role':'system',
                    'content':f"""You are a document analyst
                    Answer only based on provided document context {context}
                    If answer not in document, say I don't know"""
                },
                {
                    'role':'user',
                    'content':f'{question}'
                }
            ],
            model='llama-3.3-70b-versatile',
    )
        answer = response.choices[0].message.content
        return str(answer)
    except APIConnectionError:
        raise HTTPException(
            status_code=503,
            detail='Cannot reach Groq API — network may be blocking it!'
            )
    except APIStatusError as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=f'Groq API Error {e.message}'
            )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail='Unexpected error!'
        )


#def check_groq_connection(question: str) -> str:
#    response = client.chat.completions.create(
#        messages=[
#            {
#                'role':'system',
#                'content':'You will act as a service that will tell if you are reachable or not'
#            },
#            {
#                'role':'user',
#                'content':'Are you reachable'
#            }
#        ],
#        model=''
#    )
#    if response.choices[0].message.
#    raise HTTPException(status_code=503,detail='Groq service is not available')