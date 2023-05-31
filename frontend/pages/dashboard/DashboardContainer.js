import styles from '../../styles/Dashboard/DashboardContainer.module.css';
import DashboardInnerContainer from './DashboardInnerContainer';

function DashboardContainer() {
  return (
    <div className={styles['dashboard-container']}>
      <DashboardInnerContainer />
    </div>
  )
}

export default DashboardContainer;
