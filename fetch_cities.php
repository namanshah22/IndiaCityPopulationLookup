<?php
$host = "localhost";
$db = "my_database";
$user = "root";
$pass = "";

$pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);

if (isset($_POST['term'])) {
    $term = $_POST['term'] . '%';
    $stmt = $pdo->prepare("SELECT * FROM cities WHERE name LIKE :term");
    $stmt->execute(['term' => $term]);

    $results = [];
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        $results[] = [
            'label' => $row['name'],
            'value' => $row['name'],
            'rank' => $row['rank'],
            'population_2011' => $row['population_2011'],
            'population_2001' => $row['population_2001'],
            'state_or_union_territory' => $row['state_or_union_territory']
        ];
    }

    echo json_encode($results);
} else {
    echo json_encode([]);
}
?>
