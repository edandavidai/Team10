"""
Description: takes two lists of requests from organizations and from units and pairs them using a weighted maximal matching algorithm. Weights are based on both priority and number of people provided 
Parameters: org_requests - table with columns ID, ORG, NUM_PEOPLE, DATE
            unit_requests - table with ID, UNIT, ORG_ID, PRIORITY
            
Returns: list of pairs (org_requests_id, unit_requests_id)
            
"""    
