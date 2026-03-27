from fastapi import FastAPI
from models import attrition_model, hiring_model, role_model, tenant_model, user_model, document_model, theme_model
from database import BaseClass, engine
from controllers import agentic_router
app = FastAPI()

@app.get("/health")
async def healthCheck():
    return "Route working"

@app.on_event("startup")
def create_tables_if_not_exists():
    try:
        engine.connect()
        BaseClass.metadata.create_all(bind=engine)
        print("DB connected!")
        
        #Routers
        app.include_router(agentic_router, prefix="/agent")
    except Exception as e:
        print("Not able to connect DB!", e)