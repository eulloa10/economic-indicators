import styles from '../styles/Modals/SignInModal.module.css'

function SignInModal({setShowSignIn}) {
  return (
    <div className={styles['signin-modal-container']}>
      <form className={styles['signin-form']}>
      <h2 className={styles['signin-form-title']}>State of the Market</h2>
      <p className={styles['signin-form-title']}>Sign in with email</p>
      <div className={styles['signin-data-inputs']}>
        <div className={styles['signin-email-input']}>
          <label className={styles['signin-labels']} for="email">Email</label>
          <input className={styles['signin-input-boxes']} type="email" name="email" id="email" required/>
        </div>
        <div className={styles['signin-password-input']}>
          <label className={styles['signin-labels']} for="password">Password</label>
          <input className={styles['signin-input-boxes']} type="password" name="password" id="password" required/>
        </div>
      </div>
      <div>
        <p className={styles['create-account-link']}>Register as new user</p>
      </div>
      <button onClick={() => setShowSignIn(false)}>Sign In</button>
      </form>
    </div>
  )
}

export default SignInModal;
