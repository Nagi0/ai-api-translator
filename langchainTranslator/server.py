from langchainTranslator.chain import chain
from fastapi import FastAPI
from langserve import add_routes
import uvicorn


app = FastAPI(
    title="Lang-Chain Server",
    description="Traduza qualquer texto para qualquer idioma.",
)
add_routes(app, chain, path="/tradutor")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9000)
