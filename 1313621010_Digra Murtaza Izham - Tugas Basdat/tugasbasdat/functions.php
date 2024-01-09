<?php 
    //connect ke database
    $db = mysqli_connect("localhost", "root", "", "my_playlist");
    
    function query( $query ){
        global $db;
        $result = mysqli_query($db, $query);
        $rows = [];
        while ( $row = mysqli_fetch_assoc($result) ) {
            $rows[] = $row;
        }
        return $rows;
    }

    function insert( $data ){
        global $db;
        $title = htmlspecialchars($data["title"]);
        $year_release = htmlspecialchars($data["year"]);
        $singer = htmlspecialchars($data["singer"]);
        $genre = htmlspecialchars($data["genre"]);

        $insert = "INSERT INTO playlist (title, year, singer, genre)
                    VALUES
                    ('$title', '$year_release', '$singer', '$genre') ";
        mysqli_query($db, $insert);
        return mysqli_affected_rows($db);
    }
?>