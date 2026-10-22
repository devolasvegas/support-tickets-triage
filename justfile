[private]
default:
    @just --list --unsorted

# Start Postgres and wait until healthy
db:
    docker compose up -d --wait

# Shut down the container, keep data
db-down:
    docker compose down

# Shut down the container and wipe data, then re-run init SQL
[confirm("Delete the database volume and all data?")]
db-reset:
    docker compose down -v && docker compose up -d --wait

# Open a psql shell in the dev database
db-psql:
    docker compose exec db sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"'
