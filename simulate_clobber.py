def player_name(n):
    if n == 0: return "Alice"
    else:      return "Bob"

# Returns G with v removed
def strip_vertex(G,v):
    return {edge for edge in G if edge[0] != v and edge[1] != v}

# Returns the current vertex set of G
def get_vertices(G):
    out = set()
    for edge in G:
        out.add( edge[0] )
        out.add( edge[1] )
    return out

"""
Simulate clobber on G by playing every game.
Returns 0 if Alice won, and 1 if Bob won.
Player variable indicates the current turn.
Extremely inefficient, will take forever for large graphs.
"""
def simulate(G, player=0, misere=False, loud=False):
    if loud: print("Simulating", G, "for", player_name(player))

    other_player = (player+1)%2
    vs = get_vertices(G)

    # If there are no moves, player lost
    if len(vs) == 0:
        if misere:
            return player
        else:
            return other_player
    
    # Otherwise, try making each move
    # If any subsimulation was a win for player, player makes
    # the move that led to that win, and wins this simulation.
    # Otherwise they had no winning strat, and lost.
    if any( player == simulate(strip_vertex(G,v), other_player, misere, loud) 
           for v in vs ):
        return player
    else: 
        return other_player

# ============================================================================
# User line - above this is internals
# ============================================================================

def clobber_normal(G):
    print(player_name(simulate(G)), "wins normal for graph", G)

def clobber_misere(G):
    print(player_name(simulate(G, misere=True)), "wins misere for graph", G)

clobber_normal({(0,3),(1,3),(2,3),(3,4),(4,5)})
clobber_misere({(0,1),(1,2),(2,3),(3,4),(4,5)})