//"URLify": Write a method to replace all spaces in a string with '%20'. You may assume that the
// string has sufficient space at the end to hold the additional characters, and that you are
// given the "true" length of the string.

public class ProblemThree {

  public static String twentyString(String inputString) {
    char[] inputToArray = inputString.toCharArray();
    String replaceString = "%20";
    StringBuilder str = new StringBuilder(inputToArray[0]);
//    StringBuilder stringBuilder = new StringBuilder(inputString);
    for (int i=0; i<inputToArray.length; i++) {
      if (inputToArray[i] == ' ') {
        str.append(replaceString);
      } else {
        str.append(inputToArray[i]);
      }
    } return str.toString();

  }

  public static void main(String[] args) {
    String thingy = twentyString("fifty nifty");
    System.out.println(thingy);
  }
}