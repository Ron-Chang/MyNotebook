<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello World</title>
</head>
<body>
    <?php

    echo "Hello, World!";
    echo "<br>";

    $myvar = "This is my variable.";
    echo $myvar;
    echo "<br>";

    $number_1 = 5;
    $number_2 = 7;
    $sum = $number_1 + $number_2;
    echo $sum;
    echo "<br>";

    $name = "Ron";
    echo "Hello, " . $name."!";
    echo "<br>";

    $loggedIn = 1;
    if ($loggedIn == true){
        echo "You are logged in";
    }else{
        echo "Please log in";
    };
    echo "<br>";

    $people = array("Ano", "Ron", "Catherine");
    print_r($people);
    echo "<br>";
    echo $people[2];
    echo "<br>";

    foreach ($people as $i){
        echo $i . ' ';
    };
    echo "<br>";

    $numbers = array(5, 3, 7);
    $sum = 0;
    foreach ($numbers as $number){
        $sum = $sum + $number;
    }
    echo $sum;
    echo "<br>"


    ?>
    <form action="process.php" method="post">
        Enter your name: <input name="user_name" type="text">
        <input type="submit">
    </form>
</body>
</html>
