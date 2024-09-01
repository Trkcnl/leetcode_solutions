#include <cstdlib>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode node_sum = ListNode();
        ListNode temp_node = ListNode();

        int add = 0;
        int next_val = 0;

        node_sum.val = l1->val + l2->val + add;
        if(node_sum.val > 10) {
            node_sum.val = node_sum.val % 10;
            add = 1;
        }

        l1 = l1->next;
        l2 = l2->next;
        temp_node = node_sum;
        
        while (l1 != nullptr) {
            int next_val = l1->val + l2->val + add;

            if(next_val >= 10) {
                add = 1;
                next_val = next_val % 10;
            }

            ListNode next_node;
            next_node.val = next_val;
            next_node.next = nullptr;
            temp_node.next = &next_node;
            temp_node = *temp_node.next;
        }

        return &node_sum;
    }
};