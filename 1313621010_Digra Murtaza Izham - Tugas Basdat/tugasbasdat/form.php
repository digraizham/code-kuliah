<?php 
    require "functions.php";
    if( isset($_POST["submit"])) {
        if( insert($_POST) > 0) {
            echo "
            <script>
                alert('Data berhasil ditambahkan!');
                document.location.href='index.php';
            </script>
            ";
        }
        else {
            echo "
            <script>
                alert('Data gagal ditambahkan!');   
            </script>";
            echo mysqli_error($db);
        }
    }
?>

<!DOCTYPE html>
<html>
<head>
    <title>New Watchlist</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"
		integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
    <link rel="stylesheet" href="styles.css?v=<?php echo time(); ?>">
</head>

<body id="form">
    <div style="margin-top: 30px">
        <h2 id="form-header">Add a new song in playlist!</h2>
        <div class="container">
            <form action="" method="post">
                <div class="form-group">
                    <label for="exampleInputEmail1">Title</label>
                    <input name="title" placeholder="Input song title" type="text" class="form-control">
                </div>
                <div class="form-group">
                    <label for="inputYear">Year Release</label>
                    <input name="year" placeholder="Input song release year" type="text" class="form-control" id="inputYear">
                </div>
                <div class="form-group">
                    <label for="inputDirector">Singer</label>
                    <input name="singer" placeholder="Input name of the singer" type="text" class="form-control" id="inputSinger">
                </div>
                <div class="form-group">
                    <label for="showType">Song Genre</label>
                    <select name="genre" class="form-control" id="songGenre">
                        <option>Pop</option>
                        <option>Country</option>
                        <option>Edm</option>
                        <option>Rock</option>
                    </select>
                </div>
                <div class="d-flex justify-content-center">
                    <div class="row">
                        <div class="col-4">
                            <a class="btn btn-primary" id="cancel-btn" href="index.php"><p class="cancel">Cancel</p></a>
                        </div>
                        <div class="col-2"></div>
                        <div class="col-4">
                            <button name="submit" type="submit" class="btn btn-primary" id="submit-btn">Submit</button>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</body>
</html>