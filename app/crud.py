from app.database import database


async def get_taxonomy(taxonomy_id: int):
    query = "SELECT * FROM taxonomy_data WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": taxonomy_id})


async def add_taxonomy(taxonomy: dict):
    query = "INSERT INTO taxonomy_data (taxonomy_level, result_data) VALUES (:taxonomy_level, :result_data)"
    await database.execute(query=query, values=taxonomy)
    return {"message": "Data added successfully"}
