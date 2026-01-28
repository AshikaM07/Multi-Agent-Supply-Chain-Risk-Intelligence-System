# analysis_agent/planner.py

from db import driver, find_alternative_suppliers

def get_supplier_id_by_name(name: str):
    """
    Fetch supplier ID from Neo4j using supplier name.
    """
    with driver.session() as session:
        result = session.run(
            "MATCH (s:Supplier {name:$name}) RETURN s.id AS id",
            name=name
        )
        record = result.single()
        return record["id"] if record else None


def plan_alternatives(supplier_id: int):
    """
    Return alternative suppliers using graph traversal.
    """
    return find_alternative_suppliers(supplier_id)
