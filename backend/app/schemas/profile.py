from datetime import datetime
from uuid import UUID

from pydantic import (BaseModel,ConfigDict,Field)

from app.models.profile import UserRole


class ProfileBase(BaseModel):

    full_name: str | None = Field(
        default=None,
        max_length=150
    )

    phone: str | None = Field(
        default=None,
        max_length=20
    )

    avatar_url: str | None = None


class ProfileUpdate(ProfileBase):

    model_config = ConfigDict(
        extra="forbid"
    )


class ProfileResponse(ProfileBase):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID

    role: UserRole

    is_active: bool

    created_at: datetime

    updated_at: datetime