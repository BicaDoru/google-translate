<?php

$host = '172.19.23.203';
$port = 8886;

$socket = socket_create(AF_INET, SOCK_STREAM, 0) or die("Could not create socket\n");
$result = socket_connect($socket, $host, $port) or die("Could not connect to server\n");

echo "Enter words to be translated (or type 'quit' to exit):\n";

while (true) {
    $word = readline("Word: ");
    if ($word === 'quit') {
        break;
    }

    socket_write($socket, $word, strlen($word)) or die("Could not send data to server\n");
    $response = socket_read($socket, 1024, PHP_NORMAL_READ) or die("Could not read server response\n");
    echo "Translation: " . $response . "\n";
}

socket_close($socket);

?>

