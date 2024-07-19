
// Message Timer

var message_timeout = document.getElementById("message-timer")
setTimeout(function() {message_timeout.style.display = "none"}, 3000);

//
// <script type="text/javascript">
//        window.onpageshow = function(event) {
//            if (event.persisted || (window.performance && window.performance.navigation.type === 2)) {
//                window.location.href = "{% url 'core:dashboard' %}";
//            }
//        };
//    </script>

