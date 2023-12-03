package Solutions;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * day3
 */

public class day3 {
    public static void main(String[] args) throws IOException {
        List<String> lines = readFromFile();
        char[][] map = new char[lines.size()][lines.get(0).length()];
        for (int i = 0; i < lines.size(); i++) {
            map[i] = lines.get(i).toCharArray();
        }
        part1(map);
    }

    public static class Number {
        List<int[]> coords = new ArrayList<>();
        int startCol;
        int endCol;
        int startRow;
        int endRow;
        String number;
        int id;

        public Number(int startCol, int endCol, int startRow, int endRow, Character number) {
            this.startCol = startCol;
            this.endCol = endCol;
            this.startRow = startRow;
            this.endRow = endRow;
            this.number = number.toString();
            coords.add(new int[] { startCol, startRow });
        }

        public void setEndCoords(int endCol, int endRow) {
            this.endCol = endCol;
            this.endRow = endRow;
            coords.add(new int[] { endCol, endRow });
        }

        public void appendDigit(Character digit) {
            this.number += digit;
        }

        public boolean checkIfCellIsInNumber(int col, int row) {
            for (int[] coords : this.coords) {
                if (coords[0] == col && coords[1] == row) {
                    return true;
                }
            }
            return false;
        }

    }

    public static void part1(char[][] map) {
        List<Number> numbers = new ArrayList<>();
        int id = 0;
        int total = 0;
        int rows = map.length;
        int cols = map[0].length;
        boolean newNumber = true;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (Character.isDigit(map[i][j])) {
                    if (newNumber) {
                        numbers.add(new Number(j, j, i, i, map[i][j]));
                        newNumber = false;
                    } else {
                        numbers.get(numbers.size() - 1).setEndCoords(j, i);
                        numbers.get(numbers.size() - 1).appendDigit(map[i][j]);
                    }
                } else {
                    newNumber = true;
                }
            }
        }
        for (Number number : numbers) {
            if (checkAdjacentCells(number, map)) {
                total += Integer.parseInt(number.number);
            }
        }
        System.out.println(total);
        part2(map, numbers);
    }

    public static void part2(char[][] map, List<Number> numbers) {
        int rows = map.length;
        int cols = map[0].length;
        int total = 0;
        List<Number> localNums = new ArrayList<Number>();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (map[i][j] == '*') {
                    localNums = getNeighbours(i, j, map, numbers);
                    if (localNums.size() != 2){
                        continue;
                    }
                    int mult=1;
                    for (Number num : localNums){
                        mult*=Integer.parseInt(num.number);
                        System.out.print(num.number+" ");
                    }
                    System.out.println();
                    total+=mult;
                }
            }
        }
        System.out.println(total);
    }

    public static List<Number> getNeighbours(int i, int j, char[][] map, List<Number> numbers) {
        // Check in a 3x3 grid for a number
        int startRow = i - 1;
        int endRow = i + 1;
        int startCol = j - 1;
        int endCol = j + 1;
        List<Number> localNums = new ArrayList<Number>();
        for (int k = startRow; k <= endRow; k++) {
            for (int l = startCol; l <= endCol; l++) {
                if (k >= 0 && k < map.length && l >= 0 && l < map[0].length && Character.isDigit(map[k][l])) {
                    Number num = getNumber(k, l, map, numbers);
                    if (!localNums.contains(num)) {
                        localNums.add(num);
                    }
                }
            }
        }
        return localNums;
    }

    public static Number getNumber(int i, int j, char[][] map, List<Number> numbers) {
        for (Number num : numbers) {
            if (num.checkIfCellIsInNumber(j, i)) {
                return num;
            }
        }
        return null;
    }

    public static boolean checkAdjacentCells(Number num, char[][] map) {
        int startCol = num.startCol;
        int endCol = num.endCol;
        int startRow = num.startRow;
        int endRow = num.endRow;
        String invalidChars = "1234567890.";
        for (int i = startRow; i <= endRow; i++) {
            for (int j = startCol; j <= endCol; j++) {
                // Check top left
                if (i - 1 >= 0 && j - 1 >= 0 && invalidChars.indexOf(map[i - 1][j - 1]) == -1) {
                    return true;
                }
                // Check top
                if (i - 1 >= 0 && invalidChars.indexOf(map[i - 1][j]) == -1) {
                    return true;
                }
                // Check top right
                if (i - 1 >= 0 && j + 1 < map[0].length && invalidChars.indexOf(map[i - 1][j + 1]) == -1) {
                    return true;
                }
                // Check left
                if (j - 1 >= 0 && invalidChars.indexOf(map[i][j - 1]) == -1) {
                    return true;
                }
                // Check right
                if (j + 1 < map[0].length && invalidChars.indexOf(map[i][j + 1]) == -1) {
                    return true;
                }
                // Check bottom left
                if (i + 1 < map.length && j - 1 >= 0 && invalidChars.indexOf(map[i + 1][j - 1]) == -1) {
                    return true;
                }
                // Check bottom
                if (i + 1 < map.length && invalidChars.indexOf(map[i + 1][j]) == -1) {
                    return true;
                }
                // Check bottom right
                if (i + 1 < map.length && j + 1 < map[0].length && invalidChars.indexOf(map[i + 1][j + 1]) == -1) {
                    return true;
                }
            }
        }
        return false;
    }

    public static List<String> readFromFile() {
        try {
            BufferedReader reader = new BufferedReader(new FileReader("Inputs/day3.txt"));
            List<String> lines = new ArrayList<>();
            String line = reader.readLine();
            while (line != null) {
                lines.add(line);
                line = reader.readLine();
            }
            reader.close();
            return lines;
        } catch (Exception e) {
            System.out.println("Error reading file");
            return null;
        }
    }
}