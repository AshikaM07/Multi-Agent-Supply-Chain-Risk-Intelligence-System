// ===============================
// Neo4j Setup – Phase 1
// Supply Chain Risk Intelligence
// ===============================

// Clear existing data
MATCH (n) DETACH DELETE n;

// -------------------------------
// Suppliers (10 mock suppliers)
// -------------------------------
CREATE (:Supplier {id: 1, name: "Alpha Metals", location: "India"});
CREATE (:Supplier {id: 2, name: "Beta Steels", location: "India"});
CREATE (:Supplier {id: 3, name: "Gamma Imports", location: "China"});
CREATE (:Supplier {id: 4, name: "Delta Traders", location: "Vietnam"});
CREATE (:Supplier {id: 5, name: "Epsilon Alloys", location: "India"});
CREATE (:Supplier {id: 6, name: "Zeta Metals", location: "Germany"});
CREATE (:Supplier {id: 7, name: "Eta Industrial", location: "USA"});
CREATE (:Supplier {id: 8, name: "Theta Corp", location: "Japan"});
CREATE (:Supplier {id: 9, name: "Iota Supplies", location: "South Korea"});
CREATE (:Supplier {id: 10, name: "Kappa Manufacturing", location: "Mexico"});

// -------------------------------
// Parts
// -------------------------------
CREATE (:Part {name: "Steel Rod"});
CREATE (:Part {name: "Aluminium Sheet"});
CREATE (:Part {name: "Copper Wire"});

// -------------------------------
// Supplier → Part relationships
// -------------------------------
MATCH (s:Supplier {id: 1}), (p:Part {name: "Steel Rod"}) CREATE (s)-[:SUPPLIES]->(p);
MATCH (s:Supplier {id: 2}), (p:Part {name: "Steel Rod"}) CREATE (s)-[:SUPPLIES]->(p);
MATCH (s:Supplier {id: 3}), (p:Part {name: "Aluminium Sheet"}) CREATE (s)-[:SUPPLIES]->(p);
MATCH (s:Supplier {id: 4}), (p:Part {name: "Aluminium Sheet"}) CREATE (s)-[:SUPPLIES]->(p);
MATCH (s:Supplier {id: 5}), (p:Part {name: "Steel Rod"}) CREATE (s)-[:SUPPLIES]->(p);
MATCH (s:Supplier {id: 6}), (p:Part {name: "Steel Rod"}) CREATE (s)-[:SUPPLIES]->(p);
MATCH (s:Supplier {id: 7}), (p:Part {name: "Copper Wire"}) CREATE (s)-[:SUPPLIES]->(p);
MATCH (s:Supplier {id: 8}), (p:Part {name: "Copper Wire"}) CREATE (s)-[:SUPPLIES]->(p);
MATCH (s:Supplier {id: 9}), (p:Part {name: "Steel Rod"}) CREATE (s)-[:SUPPLIES]->(p);
MATCH (s:Supplier {id: 10}), (p:Part {name: "Aluminium Sheet"}) CREATE (s)-[:SUPPLIES]->(p);
