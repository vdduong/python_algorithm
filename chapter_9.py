# from A to B with Edsger and friends

# PROPAGATING KNOWLEDGE

# a dict of dicts representation of the graph
# a dict D to maintain distance estimates (upper bounds)
# predecessor dict P

inf = float('inf')
def relax(W, u, v, D, P): # the relaxation operation
  d = D.get(u, inf) + W[u][v] # possible shortcut estimate
  if d < D.get(v, inf): # is it really a shortcut
    D[v], P[v] = d, u
    return True # There was a change

# the Bellman-Ford algorithm, works with negative cycle graph
def bellman_ford(G, s):
  D, P = {s:0}, {} # zero-dist to s, no parents
  for rnd in G:
    changed = False # no changes in round so far
    for u in G:
      for v in G[u]:
        if relax(G, u, v, D, P):
          changed = True
    if not changed: break
  else:
    raise ValueError('negative cycle')
  return D, P

# FINDING THE HIDDEN DAG
from heapq import heappush, heappop

def dijkstra(G, s):
  D, P, Q, S = {s:0}, {}, [(0, s)], set() # Est., tree, queue, visited
  while Q:
    _, u = heappop(Q) # node with lowest estimate
    if u in S: continue # already visited ? skip it
    S.add(u)
    for v in G[u]:
      relax(G, u, v, D, P)
      heappush(Q, (D[v], v))
  return D, P









    
