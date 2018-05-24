        download_button=$("#mage_download");
        download_button.click(download);
        function download(){
        alert();
            map.once('postcompose', function(event) {
              var canvas = event.context.canvas;
              if (navigator.msSaveBlob) {
                navigator.msSaveBlob(canvas.msToBlob(), 'map.png');
              } else {
                canvas.toBlob(function(blob) {
                  saveAs(blob, 'map.png');
                });
              }
            });
            map.renderSync();
        }