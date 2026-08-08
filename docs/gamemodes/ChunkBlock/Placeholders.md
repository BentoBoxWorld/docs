# ChunkBlock placeholders

ChunkBlock registers the magic-block placeholders inherited from the AOneBlock engine, all prefixed `chunkblock_`, plus five territory placeholders of its own.

!!! tip "The five you probably want on your scoreboard"
    - `%chunkblock_island_chunks%` — chunks owned
    - `%chunkblock_island_max_chunks%` — the ceiling
    - `%chunkblock_island_chunk_credit%` — levels available to spend right now
    - `%chunkblock_island_next_chunk_level%` — the island level that buys the next chunk
    - `%chunkblock_island_ring%` — how far the territory reaches from the centre

    `credit` and `chunks` together are the whole progression at a glance: *"9 chunks, 3 to spend."*

Placeholders that read a player's **own** island resolve to the island they own, even while they are standing on someone else's. The `visited_island_*` variants read the island the player is currently on.

{{ placeholders_bundle(gamemode_name="chunkblock") }}
