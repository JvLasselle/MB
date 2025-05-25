#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct binTree {
    int key;
    int val;
    struct binTree* left;
    struct binTree* right;
} BinTree;

void preOrderTraversal(struct binTree head, int level){
    //Write your solution to this function here.
    //You may reference the function inOrderTraversal below for guidance.





}

void inOrderTraversal(struct binTree head, int level){
    //Print left side of tree.
    if (head.left != NULL){ 
        inOrderTraversal(*head.left, level+1);
    }

    //Print current tree node.
    for(int i = 0; i < level; i++){
        putchar(' ');
    }
    printf("Key: %d  \tVal: %d\n", head.key, head.val);

    //Print right side of tree.
    if (head.right != NULL){ 
        inOrderTraversal(*head.right, level+1);
    }
}

struct binTree addItem(struct binTree head, int key) {
    if (head.key == key){
        head.val++;
    } else if (head.key < key){ //Add to the right side
        if (head.right == NULL){
            head.right = (struct binTree*) malloc(sizeof(struct binTree));
            (*head.right).key = key;
            (*head.right).val = 1;
            (*head.right).left = NULL;
            (*head.right).right = NULL;
        } else {
            (*head.right) = addItem(*head.right, key);
        }
    } else { //Add to the left side
         if (head.left == NULL){
            head.left = (struct binTree*)malloc(sizeof(struct binTree));
            (*head.left).key = key;
            (*head.left).val = 1;
            (*head.left).left = NULL;
            (*head.left).right = NULL;
        } else {
            (*head.left) = addItem(*head.left, key);
        }
    }
    return head;
}

int main() {
    srand(time(NULL));
    printf("Welcome to the C Programming Language\n");
    //Init top of tree
    struct binTree head;
    head.key = rand() % 20;
    //head.key = 10;
    head.val = 0;
    head.left = NULL;
    head.right = NULL;
    printf("Displaying traversal:\n");
    //printf("Key: %d\nVal: %d\nLeft: %p\nRight: %p\n", head.key, head.val, head.left, head.right)

    //Load a bunch of data into the tree.
    for(int i=0;i<100;i++){
        head = addItem(head, rand() % 20);
    }
    preOrderTraversal(head, 0);
    
    /* Test basic functionality
    head = addItem(head, 10);
    head = addItem(head, 15);
    head = addItem(head, 15);
    head = addItem(head, 17);
    printf("Key: %d\nVal: %d\nLeft: %p\nRight: %p\n", head.key, head.val, head.left, head.right);
    head = *head.right;
    printf("\n\nStart right:\n");
    printf("Key: %d\nVal: %d\nLeft: %p\nRight: %p\n", head.key, head.val, head.left, head.right);
    */

    return 0;
}