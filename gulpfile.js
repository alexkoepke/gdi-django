gulp.task('browser-sync', function() {
    browserSync.init({
        proxy: "127.0.0.1:"
    });
});
