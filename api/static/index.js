document.getElementById('subscribe').addEventListener('click', function(e) {
    e.preventDefault();
    const popup = new bootstrap.Modal(document.getElementById('subscribe-popup'));
    popup.show();
});

const popupHTML = `
<div class="modal fade" id="subscribe-popup" tabindex="-1" aria-labelledby="subscribe-popup-label" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="subscribe-popup-label">Subscribe to our newsletter</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p>Enter your email address below to subscribe to our newsletter</p>
        <form action="https://buttondown.com/api/emails/embed-subscribe/hilliard" method="post" target="popupwindow" onsubmit="window.open('https://buttondown.com/api/emails/embed-subscribe/hilliard', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true">
          <div class="mb-3">
            <label for="email" class="form-label">Email address</label>
            <input type="email" name="email" class="form-control" id="email" aria-describedby="emailHelp">
            <input type="hidden" value="1" name="embed" />
            <input type="hidden" name="src" value="news.sntx.dev" />
            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
          </div>
          <button type="submit" class="btn btn-primary">Subscribe</button>
        </form>
      </div>
    </div>
  </div>
`;

document.body.insertAdjacentHTML('beforeend', popupHTML);
