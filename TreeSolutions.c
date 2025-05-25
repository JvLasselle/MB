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
    for(int i = 0; i < level; i++){
        putchar(' ');
    }
    printf("Key: %d  \tVal: %d\n", head.key, head.val);
    if (head.left != NULL){ 
        preOrderTraversal(*head.left, level+1);
    }
    if (head.right != NULL){ 
        preOrderTraversal(*head.right, level+1);
    }
}

void inOrderTraversal(struct binTree head, int level){
    if (head.left != NULL){ 
        inOrderTraversal(*head.left, level+1);
    }
    for(int i = 0; i < level; i++){
        putchar(' ');
    }
    printf("Key: %d  \tVal: %d\n", head.key, head.val);
    if (head.right != NULL){ 
        inOrderTraversal(*head.right, level+1);
    }
}