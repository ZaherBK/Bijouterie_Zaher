import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

os.environ['DATABASE_URL'] = "postgresql+asyncpg://neondb_owner:npg_y7eFOUEX4prG@ep-weathered-recipe-agay3m4t-pooler.c-2.eu-central-1.aws.neon.tech/hrdb?ssl=require"

from fastapi.testclient import TestClient
from app import main, deps

async def mock_user(request=None):
    return {"id": 8, "branch_id": 1, "permissions": {"is_admin": True}}

main.app.dependency_overrides[deps.get_current_session_user] = mock_user

client = TestClient(main.app)

try:
    response = client.get('/pay-employee')
    print('STATUS', response.status_code)
    if response.status_code == 500:
        print('ERROR TEXT:', response.text)
    else:
        print('SUCCESS?', len(response.text))
except Exception as e:
    import traceback
    traceback.print_exc()
