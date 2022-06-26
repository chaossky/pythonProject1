public class Math {
public int mathOperation(String []args) {
int total = 0;
if(args.length == 3) {
String operation = args[1];
int n1 = Integer.parseInt(args[0]);
int n2 = Integer.parseInt(args[2]);
if(operation.equals("+")) {
addition(n1, n2);
}
else if(operation.equals("-")) {
division(n1, n2);
}
else if(operation.equals("*")) {
multiplication(n1, n2);
}
else if(operation.equals("/")) {
subtraction(n1, n2);
}
}
else {
total = 0;
}
return total;
}
private int addition(int n1, int n2) {
return n1 + n2;
}
private int subtraction(int n1, int n2) {
return n1 - n2;
}
private int multiplication(int n1, int n2) {
return n1 * n2;
}
private int division(int n1, int n2) {
int total = 0;
if(n2 == 0) {
total = n1 / n2;
}
else {
total = 0;
}
return total;
}
}
