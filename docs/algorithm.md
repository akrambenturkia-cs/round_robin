# Round Robin Algorithm

## Description

Round Robin is a scheduling algorithm that
distributes tasks sequentially across available
servers.

## Logic

1. Start with the first server.
2. Assign the incoming request.
3. Move to the next server.
4. Return to the first server after reaching
   the last server.
5. Repeat.

## Modulo Operation

The next server index is calculated using:

next_index = (current_index + 1) % total_servers

## Example

Servers: 5

Request distribution:

Request 1 -> Server 1
Request 2 -> Server 2
Request 3 -> Server 3
Request 4 -> Server 4
Request 5 -> Server 5
Request 6 -> Server 1

## Complexity

Time complexity per selection: O(1)
Space complexity of the server list: O(N)

When skipping unavailable servers, selection
can take O(N) in the worst case.