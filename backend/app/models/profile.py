import enum
import uuid

from datetime import datetime

from sqlalchemy import (String,Text,Boolean,DateTime,text)

from sqlalchemy.dialects.postgresql import (UUID,ENUM)

from sqlalchemy.orm import (Mapped,mapped_column)

from app.core.base import Base


class UserRole(str, enum.Enum):

    CUSTOMER = "customer"
    MECHANIC = "mechanic"
    ADMIN = "admin"


class Profile(Base):

    __tablename__ = "profiles"

    __table_args__ = {
        "schema": "public"
    }

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True
    )

    full_name: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    avatar_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    role: Mapped[UserRole] = mapped_column(
        ENUM(
            UserRole,
            name="user_role",
            schema="public",
            create_type=False,
            values_callable=lambda roles: [
                role.value for role in roles
            ]
        ),
        nullable=False,
        server_default=text("'customer'")
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default=text("true")
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("now()")
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("now()")
    )