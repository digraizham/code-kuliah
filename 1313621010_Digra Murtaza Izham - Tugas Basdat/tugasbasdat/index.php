<?php 
    require "functions.php";

    //ambil data (query) dari tabel mahasiswa
    $query = query("SELECT * FROM playlist;");
?>
<style><?php include 'styles.css'; ?></style>

<!DOCTYPE html>
<html>
<head>
    <title>my playlist</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" 
        rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" 
        crossorigin="anonymous">
    <link rel="stylesheet" href="styles.css?v=<?php echo time(); ?>">
</head>
<body>
    <div style="margin-top: 30px">
        <p id="title">My Song Playlist</p>
        <div class="container">
            <table class="table table-striped">
                <thead class="table-head">
                    <tr>
                        <th scope="col">No</th>
                        <th scope="col">Title</th>
                        <th scope="col">Year Release</th>
                        <th scope="col">Singer</th>
                        <th scope="col">Genre</th>
                    </tr>
                </thead>
                <tbody>
                    <?php $i=1; ?>
                    <?php foreach( $query as $row ) : ?>
                    <tr>
                        <th scope="row"> <?= $i ?> </th>
                        <td> <?= $row["title"] ?> </td>
                        <td><?= $row["year"] ?></td>
                        <td><?= $row["singer"] ?></td>
                        <td><?= $row["genre"] ?></td>
                    </tr>
                    <?php $i++ ?>
                    <?php endforeach; ?>
                </tbody>
            </table>
            
            <center><button type="button" id="form-btn" class="btn btn-primary btn-lg text-center" onclick="location.href='form.php'">Add New Song</button></center>
                
        </div>
    </div>
    <script 
        src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" 
        integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" 
        crossorigin="anonymous">
    </script>
</body>
</html>