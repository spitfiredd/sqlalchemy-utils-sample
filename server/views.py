from alembic_utils.pg_view import PGView


PremiumUserViewAlembic = PGView(
    schema="public",
    signature="premium_views",
    definition='SELECT * FROM "user" WHERE premium_user IS TRUE'
)