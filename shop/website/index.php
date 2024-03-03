<?php
$json = file_get_contents('http://flask-app:5000/measure_round_trip_time');
$data = json_decode($json, true);

$rtt_values = $data['rtt_values'];
$average_round_trip_time = $data['average_round_trip_time'];
$confidence_interval = $data['confidence_interval'];

?>

<html>
<head>
    <title>RTT Data</title>
</head>

<body>
    <h1>Round Trip Time Data</h1>

    <h2>RTT Values:</h2>
    <ul>
        <?php
        foreach ($rtt_values as $rtt) {
            echo "<li>$rtt</li>";
        }
        ?>
    </ul>

    <h2>Average Round Trip Time:</h2>
    <p><?php echo $average_round_trip_time; ?> seconds</p>

    <h2>Confidence Interval:</h2>
    <p><?php echo "Lower Bound: " . $confidence_interval[0] . ", Upper Bound: " . $confidence_interval[1]; ?></p>
</body>
</html>

