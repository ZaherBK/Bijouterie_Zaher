from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from ..schemas import PayOut
from ..models import Pay, Employee, User
from ..auth import api_require_permission
from ..deps import get_db, api_current_user

router = APIRouter(prefix="/api/pay", tags=["pay"])

@router.get("/", response_model=List[PayOut])
async def list_payments(
    branch_id: int | None = None,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(api_current_user)
):
    """List all payments."""
    query = select(Pay).options(selectinload(Pay.employee), selectinload(Pay.creator)).order_by(Pay.date.desc())
    
    if not user.permissions.is_admin:
        query = query.join(Employee).where(Employee.branch_id == user.branch_id)
    else:
        if branch_id:
            query = query.join(Employee).where(Employee.branch_id == branch_id)
            
    res = await db.execute(query)
    return res.scalars().all()
