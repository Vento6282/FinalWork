void FillArray(string [] array) // процедура заполнения массива
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.WriteLine($"Введите {i+1} элемент массива:");
        array[i] = Console.ReadLine();
    }
}
string [] ArrayProcessing(string [] array) // функция обработки исходного массива и создание нового массива
{
    string [] result = new string [Size(array)];
    int counter = 0;
    if (result.Length > 0)
    {
        for (int i = 0; i < array.Length; i++)
            if (array[i].Length <=3)
            {
                result[counter] = array[i];
                counter = counter + 1;
            }
    }
    return result;
}
int Size (string [] array) // функция подсчёта количества элементов массива, которые состоят из трёх или менее символов
{
    int size = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i].Length <=3)
            size = size + 1;
    }   
    return size;
}
void PrintArray(string [] array)
{
    string strArray = "[";
    for (int i = 0; i < array.Length; i++)
    {
        if (i+1 != array.Length) // проверка, не является ли текущий элемент послоедним в массиве
            strArray = strArray + "\"" + array[i] + "\",";
        else 
            strArray = strArray + "\"" + array[i] + "\"";
    }
    strArray = strArray + "]";
    Console.WriteLine(strArray);
}
Console.WriteLine("Введите количество элементов исходного массива:");
int size = Convert.ToInt32(Console.ReadLine());
string [] array  = new string [size];
FillArray(array); 
Console.WriteLine("Исходный массив:");
PrintArray(array);
string [] newArray = ArrayProcessing(array);
Console.WriteLine("Обработанный массив:");
PrintArray(newArray);