<?php
// Phase 6 - PHP Session Upload Progress & LFI Lab
echo "<h1>[LAB] Target Web Application (PHP " . PHP_VERSION . ")</h1>";
echo "<p>Status: Running on <code>" . $_SERVER['SERVER_SOFTWARE'] . "</code></p>";

// Classic Local File Inclusion (LFI) parameter
if (isset($_GET['page'])) {
    echo "<div style='background:#f0f0f0; padding:10px; border-left:4px solid #2196F3;'>";
    echo "<strong>Including requested file:</strong> " . htmlspecialchars($_GET['page']) . "<br>";
    echo "</div><hr>";
    include($_GET['page']);
} else {
    echo "<p>Navigate: <a href='?page=about.php'>About Page</a></p>";
}
