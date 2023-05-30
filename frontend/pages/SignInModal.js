import { useState } from 'react';

import styles from '../styles/Modals/SignInModal.module.css'

function SignInModal({setShowSignIn}) {
  const [showSignUp, setShowSignUp] = useState(false);

  function toggleSignUp(e) {
    e.preventDefault();
    setShowSignUp(!showSignUp)
  }
  return (
    <div className={styles['signin-modal-container']}>
      <form className={styles['signin-form']}>
      <h2 className={styles['signin-form-title']}>State of the Market</h2>
      <p className={styles['signin-form-title']}>{!showSignUp ? "Sign in with email" : "Create a new account"}</p>
      <div className={styles['signin-data-inputs']}>
        <div className={styles['signin-email-input']}>
          <label className={styles['signin-labels']} for="email">Email</label>
          <input className={styles['signin-input-boxes']} type="email" name="email" id="email" required/>
        </div>
        <div className={styles['signin-password-input']}>
          <label className={styles['signin-labels']} for="password">Password</label>
          <input className={styles['signin-input-boxes']} type="password" name="password" id="password" required/>
        </div>
        { showSignUp && <div className={styles['signin-password-input']}>
          <label className={styles['signin-labels']} for="password">Confirm password</label>
          <input className={styles['signin-input-boxes']} type="password" name="password" id="password" required/>
        </div>}
      </div>
      <div className={styles['create-account-link-container']}>
        <button onClick={toggleSignUp} className={styles['create-account-btn']}>
          {!showSignUp ? "Register as new user?" : "Sign in with existing account?"}
        </button>
      </div>
      {!showSignUp && <button className={styles['signin-submit-btn']} onClick={() => setShowSignIn(false)}>Sign in</button>
      }
      {showSignUp && <button className={styles['signin-submit-btn']} onClick={() => setShowSignIn(false)}>Create account</button>
      }
      showSignUp && <button className={styles['signin-submit-btn']} onClick={() => setShowSignIn(false)}>Proceed as guest</button>
      </form>
    </div>
  )
}

export default SignInModal;
