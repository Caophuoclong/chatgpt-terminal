<a name="readme-top"></a>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#session-token-authentication">Session Token Authentication</a></li>
  </ol>
</details>



<!-- SESSION TOKEN AUTHENTICATION -->
## Session Token Authentication

The session token can be located manually by inspecting the browser.

1. Navigate to `https://platform.openai.com/account/api-keys` in your web browser.
2. Chose `Create new secret key`.
3. Then open the file .env in the root directory and paste the copied `secret key` value into the appropriate field.
  
  ```sh
    API_KEY=session_token_value
  ```
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>