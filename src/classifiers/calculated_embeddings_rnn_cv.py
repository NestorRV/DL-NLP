from src.classifiers.calculated_embeddings_rnn import calculated_embeddings_rnn
from src.util.utilities import *


def calculated_embeddings_rnn_cv(train_xs, train_ys, test_xs, test_ys=None, verbose=1):
    own_set_seed()

    model_name = "calculated_embeddings_rnn"

    new_train_xs = np.concatenate((np.array(train_xs), np.array(test_xs)))
    new_train_ys = np.concatenate((np.array(train_ys), np.array(test_ys)))

    df_metrics = pd.DataFrame()

    data_k_fold = k_fold_cross_validation(new_train_xs, new_train_ys)
    for train_xs, train_ys, val_xs, val_ys in data_k_fold:
        labels_fold_i = calculated_embeddings_rnn(train_xs, train_ys, val_xs, val_ys, verbose)
        metrics_i = evaluate(val_ys, labels_fold_i, model_name)

        df_metrics = df_metrics.append(metrics_i, ignore_index=True)

    return pd.DataFrame({model_name: df_metrics.mean(axis=0)}).T