from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware


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

    return app


app = create_app()
