const gulp = require('gulp')
const terser = require('gulp-terser');
const imagemin = require('gulp-imagemin');
const del = require('del');

gulp.task('copy', async function () {
    gulp.src('./src/views/*.html').pipe(gulp.dest('./dist/views'))
    gulp.src('./src/css/*.css').pipe(gulp.dest('./dist/css'))
    gulp.src('./src/lib/*').pipe(gulp.dest('./dist/lib'))
    gulp.src('./src/manifest.json').pipe(gulp.dest('./dist'))
})

gulp.task('clean', async function () {
    del(['./dist/*'])
})

gulp.task('uglify', async function () {
    gulp.src('./src/js/*.js')
        .pipe(terser())
        .pipe(gulp.dest('./dist/js'));
})

gulp.task('compress-img', async function () {
    gulp.src('./src/images/*')
        .pipe(imagemin())
        .pipe(gulp.dest('./dist/images'))
})

gulp.task('build', gulp.series('copy', 'uglify', 'compress-img'))

gulp.task('watch', async function () {
    gulp.watch('./src/views/*.html', gulp.series('copy'))
    gulp.watch('./src/css/*.css', gulp.series('copy'))
    gulp.src('./src/lib/*').pipe(gulp.dest('./dist/lib'))
    gulp.watch('./src/manifest.json', gulp.series('copy'))
    gulp.watch('./src/js/*.js', gulp.series('uglify'))
    gulp.watch('./src/images/*', gulp.series('compress-img'))
})

gulp.task('default', gulp.series('build', 'watch'))