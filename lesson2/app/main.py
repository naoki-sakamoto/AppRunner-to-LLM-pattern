import os
from os.path import join, dirname
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


def create_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/")
    def read_root():
        """
        ルートパスにアクセスした際のレスポンスを返します。
        """
        return {"message": "Hello, World!"}

    @app.get("/gpt")
    def gpt(content: str):
        from openai import OpenAI

        client = OpenAI()
        try:
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": content},
                ],
            )
            return completion.choices[0].message
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return app


app = create_app()
