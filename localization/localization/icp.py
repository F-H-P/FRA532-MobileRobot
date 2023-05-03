import numpy as np
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

def fit_p_to_q(p, q):

	if p.shape == q.shape:

		(N, d) = p.shape

		# Normalize clould points by subtracting for each of them their mean points
		mean_p = np.mean(p, axis = 0)
		mean_q = np.mean(q, axis = 0)
		p_norm = p - mean_p
		q_norm = q - mean_q

		# Correlation matrix
		H = np.zeros((d, d))
		for i in range(N):
			x = p_norm[i, :]
			x = x.reshape((d, 1))

			y = q_norm[i, :]
			y = y.reshape((1, d))

			H += np.matmul(x, y)

		# SVD of H
		U, sigma, VT = np.linalg.svd(H, full_matrices = True)

		# Rotation matrix
		R_hat = np.matmul(VT.T, U.T)

		# Translation vector
		#T_hat = mean_q - np.matmul(R_hat, mean_p)

		t_hat = mean_q.T - np.matmul(R_hat, mean_p.T)

		# Homogeneous transformation
		T = np.identity(d + 1)
		T[:d, :d] = R_hat
		T[:d, d] = t_hat

		return T, R_hat, t_hat

	else:

		R_hat = np.zeros((d, d))
		t_hat = np.zeros(d)
		T = np.identity(d + 1)
		T[:d, :d] = R_hat
		T[:d, d] = t_hat
		return T, R_hat, t_hat


def iterative_closest_point(p, q, low_x, low_y, high_x, high_y, max_iter = 50, tol = 1e-5):

	d = p.shape[1]

	p_hom = np.ones((d + 1, p.shape[0]))
	q_hom = np.ones((d + 1, q.shape[0]))
	p_hom[:d,:] = np.copy(p.T)
	q_hom[:d,:] = np.copy(q.T)

	prev_error = 0

	plt.scatter(p[:, 0], p[:, 1], marker = 'o')
	plt.scatter(q[:, 0], q[:, 1], marker = '^')
	plt.show()

	for i in range(max_iter):

		# find correspondence between the two cloud points
		nn = NearestNeighbors(n_neighbors = 1)
		nn_fit = nn.fit(q_hom[:d, :].T)
		distances, indices = nn_fit.kneighbors(p_hom[:d, :].T)

		# flatten the returned distances and indices arrays
		distances, indices = distances.ravel(), indices.ravel()
		
		# fit p cloud point to q cloud point
		T, R_hat, t_hat = fit_p_to_q(p_hom[:d, :].T, q_hom[:d, indices].T)

		# update the p cloud point
		p_hom = np.matmul(T, p_hom)

		# find error of current assignment
		current_error = np.mean(distances)

		print('Iteration {} - Mean Distance: {}'.format(i, round(current_error, 2)))

		p_new = p_hom.T[:,:d]
		q_new = q_hom.T[:,:d]

		# plt.scatter(p_new[:, 0], p_new[:, 1], marker = 'o')
		# plt.scatter(q_new[:, 0], q_new[:, 1], marker = '^')
		# plt.show()

		if np.abs(current_error - prev_error) < tol:
			break

		prev_error = current_error

	p_new = p_hom.T[:,:d]

	return T, distances, p_new