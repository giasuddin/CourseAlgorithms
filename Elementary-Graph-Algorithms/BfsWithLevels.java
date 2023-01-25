import java.util.LinkedList;

public class BfsWithLevels {

    private int numOfVertices;
    private LinkedList<Integer> adj[];

    public BfsWithLevels(int n) {
        numOfVertices = n;
        adj = new LinkedList[numOfVertices];
        for (int i = 0; i < numOfVertices; i++) {
            adj[i] = new LinkedList<>();
        }
    }

    public void addEdge(int v, int w) {
        if (!adj[v].contains(w))
            adj[v].add(w);
        if (!adj[w].contains(v))
            adj[w].add(v);
    }

    void BFS(int s) {
        boolean visited[] = new boolean[numOfVertices];
        LinkedList<Integer> queue = new LinkedList<>();

        visited[s] = true;
        queue.add(s);

        boolean nextLineFlag = false;
        int levels = 1;

        System.out.print(levels + ") ");
        while (queue.size() != 0) {
            int curNode = queue.poll();
            System.out.print(curNode + " ");

            int curNodeNeighborsSize = adj[curNode].size();
            for (int i = 0; i < curNodeNeighborsSize ; i++) {
                int neighbor = adj[curNode].get(i);
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.add(neighbor);
                    nextLineFlag = true;
                }
            }
            if (nextLineFlag) {
                nextLineFlag = false;

                System.out.println();
                levels++;
                System.out.print(levels + ") ");
            }
        }
    }

    public static void main(String args[])
    {
        BfsWithLevels g = new BfsWithLevels(8);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 5);
        g.addEdge(3, 4);
        g.addEdge(4, 6);
        g.addEdge(4, 7);

        System.out.println("Following is Breadth First Traversal printing with levels number"+
                "(starting from vertex 0)");
        g.BFS(0);
    }
}