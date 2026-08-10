class Node {
    public:
    std::unordered_map<char, Node*> map {};
    bool end = false;
};

class PrefixTree {
public:
    Node* root;
    PrefixTree() {
        root = new Node();
    }
    
    void insert(string word) {
        Node* temp = root;
        for(auto c : word)
        {
            if(temp -> map.find(c) == temp -> map.end())
            {
                Node* newNode = new Node();
                temp -> map[c] = newNode;
            }
            temp = temp -> map[c];
        }
        temp -> end = true;
    }
    
    bool search(string word) {
        Node* temp = root;
        for(auto c : word)
        {
            if(temp -> map.find(c) == temp -> map.end()) return false;
            temp = temp -> map[c];
        }

        return temp -> end;
    }
    
    bool startsWith(string prefix) {
        Node* temp = root;
        for(auto c : prefix)
        {
            if(temp -> map.find(c) == temp -> map.end()) return false;
            temp = temp -> map[c];
        }
        return true;
    }
};
