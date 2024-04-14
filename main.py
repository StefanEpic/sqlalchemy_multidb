from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from src.apps.apps_routers import apps_routers


app = FastAPI(title="DB service", summary="", version="1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)

# for router in apps_routers:
#     app.include_router(router)
