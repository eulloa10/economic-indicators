import styles from '../../styles/Dashboard/UpdateButton.module.css';

function UpdateButton() {
  return(
    <button className={styles['update-dash-btn']}>
      Apply filters
    </button>
  )
}

export default UpdateButton;
